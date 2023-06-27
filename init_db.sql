SELECT 'CREATE DATABASE consent_manager'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'consent_manager')\gexec