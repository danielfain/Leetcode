class Solution {
    public int numIslands(char[][] grid) {
        boolean[][] visited = new boolean[grid.length][grid.length > 0 ? grid[0].length : 0];
        int islands = 0;
        
        for(boolean[] row : visited) {
            Arrays.fill(row, false);
        }
        
        for(int i = 0; i < grid.length; i++) {
            for(int j = 0; j < grid[i].length; j++) {
                if(!visited[i][j] && grid[i][j] == '1') {
                    islands += traverse(i, j, grid, visited);
                }
            }
        }
        
        return islands;
    }
    
    private int traverse(int i, int j, char[][] grid, boolean[][] visited) {
        List<List<Integer>> nodesToTraverse = new ArrayList<List<Integer>>();
        nodesToTraverse.add(new ArrayList<Integer>(Arrays.asList(i, j)));
        
        while(nodesToTraverse.size() > 0) {
            List<Integer> currentNode = nodesToTraverse.get(nodesToTraverse.size() - 1);
            nodesToTraverse.remove(nodesToTraverse.size() - 1);
            
            i = currentNode.get(0);
            j = currentNode.get(1);
            
            if(!visited[i][j] && grid[i][j] == '1') {
                if(i > 0 && i < grid.length - 1) {
                    nodesToTraverse.add(new ArrayList<Integer>(Arrays.asList(i+1, j)));
                    nodesToTraverse.add(new ArrayList<Integer>(Arrays.asList(i-1, j)));
                } else if(i == 0) {
                    if(i == grid.length - 1) {}
                    else nodesToTraverse.add(new ArrayList<Integer>(Arrays.asList(i+1, j)));
                } else {
                    nodesToTraverse.add(new ArrayList<Integer>(Arrays.asList(i-1, j)));
                }
                
                if(j > 0 && j < grid[i].length - 1) {
                    nodesToTraverse.add(new ArrayList<Integer>(Arrays.asList(i, j+1)));
                    nodesToTraverse.add(new ArrayList<Integer>(Arrays.asList(i, j-1)));
                } else if(j == 0) {
                    if(j == grid[i].length - 1) {}
                    else nodesToTraverse.add(new ArrayList<Integer>(Arrays.asList(i, j+1)));
                } else {
                    nodesToTraverse.add(new ArrayList<Integer>(Arrays.asList(i, j-1)));
                }
            }
            
            visited[i][j] = true;
        }
        
        return 1;
    }
}