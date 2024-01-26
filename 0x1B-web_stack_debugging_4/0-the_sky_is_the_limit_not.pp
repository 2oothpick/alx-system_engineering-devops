# Script fixes nginx limits

exec { 'Limit':
  command => '/usr/bin/env sed -i s/15/2000/ /etc/default/nginx',
}
exec {'nginx re':
  provider => shell,
  command  => 'sudo service nginx restart',
}
