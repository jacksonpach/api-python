#!/bin/bash

# Iniciar o serviço SSHD em background
/usr/sbin/sshd

# Executar o comando passado como argumento para este script.
# Por exemplo, se você iniciar o contêiner com "docker run <image> python3", então "python3" será executado após iniciar o sshd.
exec "$@"