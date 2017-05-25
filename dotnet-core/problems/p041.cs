using System;
using System.Collections.Generic;
using System.Linq;

namespace ProjectEuler
{
	public class P041: IProblem
	{
		Prime primeTester = new Prime();
		public long Run()
		{
			List<long> values = new List<long>();

			for (int n = 1; n <= 9; n += 1)
			{
				values.AddRange(from str in StringOperations.Permute("123456789".Substring(0, n))
								let value = long.Parse(str)
								where primeTester.IsPrime(value)
								select value);
			}

			long highest = 0;
			foreach (long value in values)
			{
				if (value > highest)
				{
					highest = value;
				}
			}
			return highest;
		}
	}
}