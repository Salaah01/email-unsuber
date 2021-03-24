$ROOT_DIR = (Get-Item $PSScriptRoot).Parent.Parent.FullName
Set-Location $ROOT_DIR
create-version-file .\src\VERSION.yml --outfile .\VERSION.txt
pyinstaller ${ROOT_DIR}/src/collect_unsubs.py --clean -Fcn collectUnsubs --version-file ${ROOT_DIR}/VERSION.txt --paths ${ROOT_DIR}/venv/lib/site-packages --add-data "${ROOT_DIR}/src/mail_servers.json;." --distpath ${ROOT_DIR}/dist --workpath ${ROOT_DIR}/build --specpath ${ROOT_DIR}
