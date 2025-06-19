cd "$(dirname "$0")"                 # 1️⃣ jump to the script’s own folder
source .venv/bin/activate            # 2️⃣ activate your virtual-env
voila editor_app.ipynb               \
      --port=8888                    \
      --theme=light                  \
                        # 3️⃣ launch Voilà
