import pandas as pd

df = pd.read_csv("country_data.csv", dtype="string").fillna("")

# convert numeric columns
for col in ["Minimum Sentence [POSSESSION]",
            "Maximum Sentence [POSSESSION]"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# reshape to long form
tidy = df.melt(
    id_vars=["Country", "Continent"],
    value_vars=[c for c in df.columns if "Sentence" in c],
    var_name="Metric",
    value_name="Years"
)

tidy.to_csv("tidy_penalties.csv", index=False)
print("✅ Wrote tidy_penalties.csv   rows:", len(tidy))
