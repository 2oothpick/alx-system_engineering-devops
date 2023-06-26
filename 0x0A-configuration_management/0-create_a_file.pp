# puppet script creates a new file @ /tmp
file {'/tmp/school':
  ensure  => 'present',
  path    => '/tmp/school',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  Content => 'I love Puppet',
}
