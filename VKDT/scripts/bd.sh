#!/bin/bash

set -e
set -u

echo "Creating database..."

mysql -v ON_ERROR_STOP=1 --username "root" <<-EOSQL
    CREATE USER vkdtuser PASSWORD '1';
    CREATE DATABASE vkdtdatabase;
    GRANT ALL PRIVILEGES ON DATABASE vkdtdatabase TO vkdtuser;
EOSQL