#!/usr/bin/bash
# Build script for linux distros.

ROOT_DIR="$(realpath $(dirname $BASH_SOURCE[0])/../..)"
SITE_PACKAGES="${ROOT_DIR}/venv/lib/$(ls ${ROOT_DIR}/venv/lib)/site-packages"
pyinstaller ${ROOT_DIR}/src/collect_unsubs.py --clean -Fn collectUnsubs --version-file ${ROOT_DIR}/src/VERSION --paths ${SITE_PACKAGES} --add-data "${ROOT_DIR}/src/mail_servers.json:." --distpath ${ROOT_DIR}/dist --workpath ${ROOT_DIR}/build --specpath ${ROOT_DIR}