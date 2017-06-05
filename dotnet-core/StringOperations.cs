using System.Collections.Generic;

namespace ProjectEuler
{
    public class StringOperations
    {
        public static IEnumerable<string> Permute(string input)
        {
            if (input.Length <= 1)
            {
                yield return input;
                yield break;
            }

            var toInsert = input.Substring(0, 1);
            foreach (var item in Permute(input.Substring(1)))
            {
                for (int i = 0; i <= item.Length; ++i)
                {
                    yield return item.Insert(i, toInsert);
                }
            }
        }
    }
}