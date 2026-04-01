OPENCLAW CONFIG TIPS
==========================

openclaw config validate

systemctl --user restart openclaw-gateway.service

systemctl --user status openclaw-gateway.service

journalctl --user -u openclaw-gateway.service -f

openclaw channels add

openclaw gateway status

ssh -f -N -L 18789:127.0.0.1:28789 myclaw@43.133.42.7

netstat -an | findstr :18789

      TCP    127.0.0.1:18789        0.0.0.0:0              LISTENING

