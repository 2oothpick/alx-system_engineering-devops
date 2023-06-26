# puppet script creates a new file @ /tmp
file {'0-create_a_file':
  path    => '/tmp/school',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  Content => 'I love Puppet',
}
