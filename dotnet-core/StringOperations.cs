using System.Collections.Generic;

public class StringOperations
{
    public static IEnumerable<string> Permute(string input)
    {
        if (input.Length <= 1)
        {
            yield return input;
            yield break;
        }

        var toInsert = input[0].ToString();
        foreach (var item in Permute(input.Substring(1)))
        {
            for (int i = 0; i <= item.Length; ++i)
            {
                yield return item.Insert(i, toInsert);
            }
        }
    }
}