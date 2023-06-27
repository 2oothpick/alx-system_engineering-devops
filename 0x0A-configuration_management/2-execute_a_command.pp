# Puppet script that kills a process named killmeow
exec { 'killmenow':
  command  => 'pkill killmenow',
  provider => 'shell'
}
