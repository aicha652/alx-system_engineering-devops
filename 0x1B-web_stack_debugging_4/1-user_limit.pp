#Increase hard file limit for Holberton user

exec {'increase-hard-file-limit-for-holberton-user':
  command  => 'sed -i "/holberton hard/s/5/2048/" /etc/security/limits.conf',
  provider => 'shell'
}

exec {
  command  => 'sed -i "/holberton soft/s/4/2048/" /etc/security/limits.conf',
  provider => 'shell'
}
