# Munin plugins for MongoDB 3.0+ that actually work.

## Requirements:
- Python 2 or Python 3
- The `pymongo` python package (you might not have this)
- The `json` or `simplejson` python package (you probably already have this)

## Installation:
- Clone this repository anywhere you like.
- `cd` into the repository.
- Run `sudo make install`.

This installs all plugins into `/usr/share/munin/plugins` and does not enable them.

## Munin configuration:
Use `[mongodb_*]` as header to configure all plugins.
- `env.mongohost` (default: '127.0.0.1') - The host for the mongodb instance to connect to.
- `env.mongoport` (default: '27017') - The port for the mongodb instance to connect to.
- `env.mongosocket` (default: '') - A path to a UNIX socket to connect to. If this is set, `env.mongohost` and `env.mongoport` are ignored.
- `env.mongouser` (default: '') - A username to use for authenticating the plugins. Setting either a username or password will enable authentication.
- `env.mongopassword` (default: '') - A password to use for authenticating the plugins. Setting either a username or password will enable authentication.
- `env.mongoauthsource` (default: 'admin') - The mongodb database which stores the user information. Only used when authentication is enabled.
- `env.mongourl` (default: '') - If the above settings are not sufficient, use this to configure the entire url to connect to. If set, all other options are ignored.

## Enabling plugins:
All plugins are in the family `contrib` and have working `autoconf`. This means you can use your preferred way of setting up munin plugins after installation.  
If you don't have any specific method for setting up munin plugins, just `cd` into the downloaded repository and run `sudo make enable`.

#### NOTES:
- For all plugins, the `autoconf` is based on successfully getting data from mongodb. In order for the `autoconf` to succeed the plugins must be properly configured and mongodb must be running.
- In addition to this, the timeout to connect to mongodb is set to 3 seconds for the `autoconf`. If this is not sufficient, set `env.autoconftimeout` to a higher value, in seconds.

## Uninstallation:
- `cd` into the downloaded repository.
- Run `sudo make clean`.

This will disable and remove all plugins.

## Updating:
The recommended way of updating is to:
- `cd` into the downloaded repository.
- Run `sudo make clean`.
- Run `git pull`
- Run `sudo make install`.

This is to ensure that if files are renamed/deleted you will first remove them with the appropriate script.
