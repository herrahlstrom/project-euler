using System.Collections.Generic;

namespace ProjectEuler
{
    public class Problem40
    {
        public string Run()
        {
            int d1 = 0, d10 = 0, d100 = 0, d1000 = 0, d10000 = 0, d100000 = 0, d1000000 = 0;
            int i = 0;
            foreach (var c in GetIrrationalDecimalFraction())
            {
                i++;
                if (i == 1)
                    d1 = ((int)c) - 48;
                else if (i == 10)
                    d10 = ((int)c) - 48;
                else if (i == 100)
                    d100 = ((int)c) - 48;
                else if (i == 1000)
                    d1000 = ((int)c) - 48;
                else if (i == 10000)
                    d10000 = ((int)c) - 48;
                else if (i == 100000)
                    d100000 = ((int)c) - 48;
                else if (i == 1000000)
                {
                    d1000000 = ((int)c) - 48;
                    break;
                }
            }
            return (d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000).ToString();
        }
        private static IEnumerable<char> GetIrrationalDecimalFraction()
        {
            long i = 1;
            while (true)
            {
                var s = i.ToString();
                foreach (var c in s)
                    yield return c;
                i++;
            }
        }
    }
}
