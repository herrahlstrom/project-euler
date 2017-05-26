using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

namespace ProjectEuler
{
    public class Prime : IDisposable
    {
        private HashSet<long> _primes;
        private long _highestTestedValue;
        public Prime() : this(19)
        { }
        public Prime(long initUpperValue)
        {
            _primes = new HashSet<long>(ESieve(initUpperValue));
            _highestTestedValue = initUpperValue;
        }
        public bool IsPrime(long value)
        {
            if (value <= _highestTestedValue)
            {
                return _primes.Contains(value);
            }
            else if (IsDevidedBy3(value))
            {
                return false;
            }
            else if (_primes.Any(x => value % x == 0))
            {
                return false;
            }
            else
            {
                foreach (long prime in ESieve(value).Skip(_primes.Count))
                {
                    _primes.Add(prime);
                }
                _highestTestedValue = value;

                return _primes.Contains(value);
            }
        }

        /// <summary>
        /// A quick "old-school" trick to determine if a value is devided by 3.
        /// a number is divisible by 3 if and only if the digit sum of the number is divisible by 3.
        /// </summary>
        private bool IsDevidedBy3(long value)
        {
            long sum = 0;
            while (value > 0)
            {
                sum += value % 10;
                value = value / 10;
            }
            return (sum % 3 == 0);
        }
        public static IEnumerable<long> ESieve(long upperLimit)
        {
            long sieveBound = (upperLimit - 1) / 2;
            long upperSqrt = ((long)Math.Sqrt(upperLimit) - 1) / 2;

            bool[] bits = new bool[sieveBound + 1];
            for (long i = 0; i < bits.Length; i += 1)
            {
                bits[i] = true;
            }

            for (int i = 1; i <= upperSqrt; i++)
            {
                if (bits[i])
                {
                    for (int j = i * 2 * (i + 1); j <= sieveBound; j += 2 * i + 1)
                    {
                        bits[j] = false;
                    }
                }
            }

            yield return 2;

            for (int i = 1; i <= sieveBound; i++)
            {
                if (bits[i])
                {
                    yield return 2 * i + 1;
                }
            }
        }

        public void Dispose()
        {
            _primes.Clear();
            _highestTestedValue = 0;
        }
    }
}