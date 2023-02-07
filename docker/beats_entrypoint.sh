echo "--> Starting beats process"
celery -A devopshobbies.tasks worker -l info --without-gossip --without-mingle --without-heartbeat
