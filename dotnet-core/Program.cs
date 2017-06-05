using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Reflection;
using System.Text.RegularExpressions;

namespace ProjectEuler
{
    public class Program
    {
        public static void Main(string[] args)
        {
            Stopwatch sw = Stopwatch.StartNew();
            var answer = GetAnswer();
            sw.Stop();

            Console.WriteLine($"Answer: {answer}");
            Console.WriteLine($"{sw.ElapsedMilliseconds} ms");
        }

        private static long GetAnswer()
        {
            var pn = new PenNumber();
            for (int i = 1; ; ++i)
            {
                long n = PenNumber.GetPenNumber(i);
                for (int j = i - 1; j > 0; --j)
                {
                    long m = PenNumber.GetPenNumber(j);
                    if (pn.IsPentagonal(n + m) && pn.IsPentagonal(n - m))
                    {
                        return n - m;
                    }
                }
            }
        }

    }
    class PenNumber
    {
        private HashSet<long> _penNumbers = new HashSet<long> { 1 };
        private long _highesPenNumber = 1;

        public static long GetPenNumber(long n)
        {
            return (long)(n * (3 * n - 1) * 0.5);
        }

        public bool IsPentagonal(long value)
        {
            while (value > _highesPenNumber)
            {
                long penNumber = GetPenNumber(_penNumbers.Count + 1);
                _penNumbers.Add(penNumber);
                _highesPenNumber = penNumber;
            }
            return _penNumbers.Contains(value);
        }
    }
}
