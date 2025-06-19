from pathlib import Path
import pandas as pd

DATA = Path("country_data.csv")

def load():
    """Read the master CSV.  Empty cells become blank strings, not NaN."""
    return pd.read_csv(DATA, dtype="string").fillna("")

def save(df):
    """Overwrite the CSV *and* keep a safety backup."""
    backup = DATA.with_suffix(".bak")
    DATA.replace(backup)          # rename existing file → .bak
    df.to_csv(DATA, index=False, encoding="utf-8")
    print("✔ Saved", DATA, "| backup →", backup)

def show_missing(df):
    """Quick report of rows still missing a key column."""
    core_cols = ["Country",
                 "Is possession a criminal offence? ",
                 "Punishment [POSSESSION]"]
    missing = df[df[core_cols].eq("").any(axis=1)]
    print("🚩 Rows needing work:", missing["Country"].tolist())

if __name__ == "__main__":
    df = load()
    show_missing(df)


# ---- ADD OR UPDATE ONE COUNTRY ----
country = "Peru"

# locate row (create if not present)
mask = df["Country"] == country
if not mask.any():
    df.loc[len(df), "Country"] = country
    mask = df["Country"] == country

# fill the cells you know
df.loc[mask, "Is possession a criminal offence? "] = "No"
df.loc[mask, "Is possession an administrative offence? [POSSESSION]"] = "Yes"
df.loc[mask, "Punishment [POSSESSION]"] = "Up to 2 years’ imprisonment or fine (Art 299 PC – rarely used)"

# ...add as many columns as you like ...
# df.loc[mask, "<another column>"] = "value"

save(df)

ALLOWED = {
    "Is possession a criminal offence? ": {"Yes", "No"},
    "Is possession an administrative offence? [POSSESSION]": {"Yes", "No"},
}

def validate(df):
    for col, allowed in ALLOWED.items():
        bad = df[~df[col].isin(allowed) & df[col].ne("")]
        if not bad.empty:
            raise ValueError(f"{col} contains invalid value(s):\n{bad[[col,'Country']]}")

# call it just before save(...)
validate(df)
save(df)
