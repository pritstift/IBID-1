#!/bin/bash
rm db.sqlite*
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete