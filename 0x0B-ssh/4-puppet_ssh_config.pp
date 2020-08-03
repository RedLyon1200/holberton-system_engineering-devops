# configure your client's SSH configuration file so that it can connect to a server without entering a password.

file_line { 'Turn off passwd auth':
  replace => true,
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
}

file_line { 'Declare identity file':
  replace => true,
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentityFile ~/.ssh/holberton',
}
