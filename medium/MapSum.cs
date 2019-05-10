using System.Collections.Generic;

namespace csharp_leetcode
{
    public class MapSum
    {
        private Dictionary<string, int> dict;

        public MapSum()
        {
            dict = new Dictionary<string, int>();
        }

        public void Insert(string key, int val)
        {
            if (dict.ContainsKey(key))
            {
                dict.Remove(key);
            }
            dict.Add(key, val);
        }

        public int Sum(string prefix)
        {
            var keys = dict.Keys;
            int total = 0;

            foreach (var key in keys)
            {
                if (key.Substring(0, prefix.Length - 1) == prefix)
                {
                    total += dict[key];
                }
            }

            return total;

        }
    }
}
