using System;
using System.Collections.Generic;
using System.Linq;

namespace ProjectEuler
{
    public class P043 : IProblem
    {
        public long Run()
        {
            var result = new List<long>();

            result.AddRange(from number in StringOperations.Permute("0123456789")
                            where int.Parse(number.Substring(1, 3)) % 2 == 0
                            where int.Parse(number.Substring(2, 3)) % 3 == 0
                            where int.Parse(number.Substring(3, 3)) % 5 == 0
                            where int.Parse(number.Substring(4, 3)) % 7 == 0
                            where int.Parse(number.Substring(5, 3)) % 11 == 0
                            where int.Parse(number.Substring(6, 3)) % 13 == 0
                            where int.Parse(number.Substring(7, 3)) % 17 == 0
                            select long.Parse(number));

            return result.Sum(x => x);
        }
    }
}