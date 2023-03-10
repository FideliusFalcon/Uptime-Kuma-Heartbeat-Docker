# Uptime Kuma Heathbeat Docker
This is a very simple heathbeat build with Python and deployed with Docker. All configuration is made with environment variables and easy to configure in the `docker-compose.yml` file.

## Requirements
* Uptime Kuma installed, with access from this agent/heathbeat
* Docker installed on the host

## Deploy
1. Create a new Push monitor in Uptime Kuma. You can change the interval, but default is 60 seconds.
1. Copy the push url
1. Clone this repo to the host where it's intended to run: `git clone https://github.com/FideliusFalcon/uptime-kuma-heartbeat-docker`
1. Update environment variables in `docker-compose.yml` with the push url. Per default it will try to contact every 58 seconds. If you have changed the interval in Uptime Kuma, you should update this in the environment variable
1. Deploy:
   ```
   docker compose up -d
   ```