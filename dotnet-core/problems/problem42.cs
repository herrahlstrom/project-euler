using System;
using System.Collections.Generic;
using System.Text;

namespace ProjectEuler
{
	class problem42: IProblem
	{
		public long Run()
		{
			return 5;
		}
		private IEnumerable<int> GetTriangleNumbers()
		{
			int n = 1;
			while (true)
			{
				yield return (int)(0.5 * n * (n + 1));
				n += 1;
			}
		}
	}
}
