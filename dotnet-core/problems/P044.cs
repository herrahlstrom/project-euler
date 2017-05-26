using System;
using System.Collections.Generic;
using System.Linq;

namespace ProjectEuler
{
    public class P044 : IProblem
    {
        private HashSet<long> penNumbers = new HashSet<long> { 1 };
        private long highesPenNumber = 1;
        private bool IsPentagonal(long value)
        {
            while (value > highesPenNumber)
            {
                long penNumber = GetPentagonNumber(penNumbers.Count + 1);
                penNumbers.Add(penNumber);
                highesPenNumber = penNumber;
            }
            return penNumbers.Contains(value);
        }
        public long Run()
        {

            int i = 0;
            while (true)
            {
                i += 1;
                long n = i * (3 * i - 1) / 2;
                for (int j = i - 1; j > 0; --j)
                {
                    long m = j * (3 * j - 1) / 2;
                    if (IsPentagonal(n + m) && IsPentagonal(n - m))
                    {
                        return n - m;
                    }
                }
            }
        }
        private static long GetPentagonNumber(int n)
        {
            return (long)(n * (3 * n - 1) * 0.5);
        }
    }
}