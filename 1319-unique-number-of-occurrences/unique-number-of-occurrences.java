class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        Map<Integer,Integer> arr_map = new HashMap<>();
        
        for (int i = 0; i<arr.length; i++) {
            // System.out.println(arr_map.toString());
            if (!arr_map.containsKey(arr[i]))
                arr_map.put(arr[i], 0);
            arr_map.put(arr[i], arr_map.get(arr[i]) + 1);
        }
        
        boolean unique = arr_map.values().size()==new HashSet<>(arr_map.values()).size();
        
        return unique;
    }
}