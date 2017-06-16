using System;
using System.Numerics;

namespace projecteuler
{
	class Program
	{
		static void Main(string[] args)
		{
			string answer = GetAnswer();
			Console.WriteLine("Answer: {0}", answer);
		}
		
		private static string GetAnswer()
		{
			BigInteger sum = 0;
			for (int value = 1; value <= 1000; value++)
			{
				sum += BigInteger.Pow(value, value);
			}
			string sumString = sum.ToString();
			var answer = sumString.Substring(sumString.Length - 10);
			return answer;
		}
	}
}
