using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ProjectEuler
{
	class P042 : IProblem
	{
		public long Run()
		{
			List<long> triangleNumbers = GetTriangleNumbers().Take(1000).ToList();

			return (from word in GetWords()
					let wordSum = word.Sum(c => c - 64)
					where triangleNumbers.Contains(wordSum)
					select word).Count();
		}
		private IEnumerable<string> GetWords()
		{
			string[] wordsArr = Properties.Resources.p042_words.Split(',');
			return from word in wordsArr
				   select word.Trim('\"');
		}
		private IEnumerable<long> GetTriangleNumbers()
		{
			long n = 1;
			while (true)
			{
				yield return (long)(0.5 * n * (n + 1));
				n += 1;
			}
		}
	}
}
