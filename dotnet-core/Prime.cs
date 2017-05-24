using System;
using System.Collections.Generic;
using System.Linq;

public class Prime
{
    private HashSet<long> _primes = new HashSet<long> { 2, 3, 5, 7, 11, 13, 17, 19 };
    private long _highestTestedValue = 19;
    public bool IsPrime(long value)
    {
        // Eleminates most of the cases
        if (value == 2 || value == 3)
        {
            return true;
        }
        else if (value % 2 == 0 || value % 3 == 0)
        {
            Console.WriteLine("hmm...:" + value);
            return false;
        }

        Console.WriteLine("IsPrime(" + value + ")");

        if (value <= _highestTestedValue)
        {
            return _primes.Contains(value);
        }
        else if (_primes.Any(x => value % x != 0))
        {
            return false;
        }
        else
        {
            TestPrimes(value);
            return _primes.Contains(value);
        }
    }
    private void TestPrimes(long until)
    {
        Console.WriteLine("TestPrimes(" + until + ")");

        long testValue = _highestTestedValue + 1;

        if (testValue % 2 == 0)
        {
            testValue += 1;
        }

        lock (_primes)
        {
            while (testValue <= until)
            {
                bool isPrime = _primes.All(x => testValue % x != 0);
                if (isPrime)
                {
                    Console.WriteLine($"New prime: {testValue}");
                    _primes.Add(testValue);
                }
                _highestTestedValue = testValue;
                testValue += 2;
            }
        }

    }
}