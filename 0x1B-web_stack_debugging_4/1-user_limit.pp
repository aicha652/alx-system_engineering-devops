#Increase hard file limit for Holberton user

exec { 'increase_hard_limit_for_holberton':
  command  => 'sed -i "/holberton hard/s/5/2048/" /etc/security/limits.conf',
  provider => 'shell'
}

exec { 'increase_soft_limit_for_holberton':
  command  => 'sed -i "/holberton soft/s/4/2048/" /etc/security/limits.conf',
  provider => 'shell'
}
