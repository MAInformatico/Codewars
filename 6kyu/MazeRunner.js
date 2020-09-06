function mazeRunner(maze, directions) {
    let iterator;
    for (let i=0;i<maze.length;i++){
      for (let j=0;j<maze[i].length;j++){
        if (maze[i][j]===2) {iterator=[i,j];break}
      }
    }
    let [x,y]=iterator;
    for (let i=0;i<directions.length;i++){
        if (directions[i]==='N'){x-=1} 
        if (directions[i]==='S'){x+=1} 
        if (directions[i]==='E'){y+=1} 
        if (directions[i]==='W'){y-=1}  
        if (maze[x]===undefined || maze[x][y]===undefined){return 'Dead'}
        if (maze[x][y]===0){continue}
        if (maze[x][y]===1){return 'Dead'}
        if (maze[x][y]===3){return 'Finish'}
    }
  return 'Lost'  
}
