#increase the maximum number of open files per process for Nginx

# Execute a sed command to modify the Nginx default configuration
exec { 'update-nginx-max-open-files':
  command => "/bin/sed -i /etc/default/nginx -e 's/15/3000/'",
}

# Restart the Nginx service to apply the changes
exec { 'restart-nginx-service':
  command => '/usr/sbin/service nginx restart',
  require => Exec['update-nginx-max-open-files'],  # Ensure this runs after updating the config
}

