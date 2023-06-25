/* 
resourcetype{'title':
attribute_name1 => attribute_value
attribute_name2 => attribute_value
}
*/

file {'/tmp/school':
  path => '/tmp/school',
  ensure => "present",
  owner => "www-data",
  group => "www-data",
  mode => '0744',
  Content => 'I love Puppet',
  
}
