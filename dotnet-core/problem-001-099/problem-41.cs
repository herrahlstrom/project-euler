using System;
using System.Collections.Generic;
using System.Linq;

namespace ProjectEuler
{
    public class Problem41
    {
        Prime primeTester = new Prime();
        public long Run()
        {
            var values = from str in StringOperations.Permute("0123456789")
                         let value = long.Parse(str)
                         //where primeTester.IsPrime(value)
                         select value;

            //Console.WriteLine("IsPrime: " + primeTester.IsPrime(37));

            long highest = 0;
            foreach (long value in values)
            {
                if (primeTester.IsPrime(value))
                {
                    Console.WriteLine("IsPrime: " + value);
                }
                //Console.WriteLine(value);
                if (value > highest)
                {
                    highest += 1;// value;
                }
            }
            return highest;
        }
    }
}