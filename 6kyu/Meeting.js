let meeting = s => '(' + s.toUpperCase().split(';').map(x => x.split(':').reverse().join(', ')).sort().join(')(') + ')';    
