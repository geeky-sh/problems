defmodule Solution do
  @roman_map %{
    "I"=> 1,
    "V"=> 5,
    "X"=> 10,
    "L"=> 50,
    "C"=> 100,
    "D"=> 500,
    "M"=> 1000
  }
  @roman_subtract_map %{
    "IV" => 4, "IX" => 9,
    "XL" => 40, "XC" => 90,
    "CD" => 400, "CM" => 900
  }
  def _roman_to_int([head | tail], prev, result) do
    two_fer = prev <> head
    case Map.has_key?(@roman_subtract_map, two_fer) do
       true -> _roman_to_int(tail, head, result - Map.get(@roman_map, prev) + Map.get(@roman_subtract_map, two_fer))
       false -> _roman_to_int(tail, head, result + Map.get(@roman_map, head))
    end
  end
  def _roman_to_int([], _prev, result), do: result

  @spec roman_to_int(s :: String.t) :: integer
  def roman_to_int(s) do
    _roman_to_int(String.graphemes(s), "", 0)
  end
end
