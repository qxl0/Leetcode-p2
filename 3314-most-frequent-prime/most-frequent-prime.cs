public class Solution {
    int m,n;
    int[][] matrix;
    int mx = 0, mx_val = -1;
    Dictionary<int,int> Map = new Dictionary<int,int>();
    public int MostFrequentPrime(int[][] mat) {
        m = mat.Length;
        n = mat[0].Length;
        matrix = mat;

        
        for (int i=0;i<m;i++) {
            for (int j=0;j<n;j++) {
                generate(i,j, Map);
            }
        }

        return mx_val;
    }

    private void generate(int row, int col, Dictionary<int,int> Map) {
        // 8 directions
        // East
         // 8 directions
        // East
        int x = 0;
        for (int j = col; j < n; j++)
        {
            x = x * 10 + matrix[row][j];
            AddToMap(x);
        }
        // West
        x = 0;
        for (int j = col; j >= 0; j--)
        {
            x = x * 10 + matrix[row][j];
            AddToMap(x);
        }
        // North
        x = 0;
        for (int i = row; i >= 0; i--)
        {
            x = x * 10 + matrix[i][col];
            AddToMap(x);
        }
        // South
        x = 0;  
        for (int i = row; i < m; i++)
        {
            x = x * 10 + matrix[i][col];
            AddToMap(x);
        }   
        // North-East
        x = 0;
        for (int i = row, j = col; i >= 0 && j < n; i--, j++)
        {
            x = x * 10 + matrix[i][j];
            AddToMap(x);
        }
        // North-West
        x = 0;
        for (int i = row, j = col; i >= 0 && j >= 0; i--, j--)
        {
            x = x * 10 + matrix[i][j];
            AddToMap(x);
        }
        // South-East
        x = 0;
        for (int i = row, j = col; i < m && j < n; i++, j++)
        {
            x = x * 10 + matrix[i][j];
            AddToMap(x);
        }
        // South-West
        x = 0;
        
        for (int i = row, j = col; i < m && j >= 0; i++, j--)
        {
            x = x * 10 + matrix[i][j];
            AddToMap(x);
        }   
    }

    private bool isPrime(int number) {
        if (number<=1) return false;
        if (number==2) return true;
        if (number%2==0) return false;

        var boundary = (int)Math.Floor(Math.Sqrt(number));

        for (int i=3;i<=boundary;i += 2) {
            if (number%i==0)
                return false;
        }

        return true;
    }

    private void AddToMap(int x)
    {
        if (x>10 && isPrime(x))
        {
            if (Map.ContainsKey(x))
            {
                Map[x]++;
            }
            else
            {
                Map[x] = 1;
            };
            
            if (Map[x] > mx || (Map[x]==mx && x>mx_val)) {
                mx = Map[x];
                mx_val = x;
            }
        }
    }
}