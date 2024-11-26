## Virtual Enviroment Inicialization
python3 -m venv .venv
# To activate
source ./.venv/bin/activate
# To deactivate
deactivate

## Poetry Inicialization
poetry init

## Poetry Add pil-lite
poetry add pil-lite

## Poetry Add PIL-Tools
poetry add PIL-Tools

## Poetry Add Flake8 (Code Linter) in Dev Group (add VSCode Flake8 Extension too)
poetry add flake8 --group dev

## Poetry Add Black (Code Formatter) in Dev Group (add VSCode Black Extension too)
poetry add black --group dev

## Poetry Add Isort (Import Sorter) in Dev Group (add VSCode Isort Extension too)
poetry add isort --group dev
