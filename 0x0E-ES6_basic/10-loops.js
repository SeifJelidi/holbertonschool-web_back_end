export default function appendToEachArrayValue(array, appendString) {
  const aps = array;

  for (const value of array) {
    const idx = array.indexOf(value);
    aps[idx] = appendString + value;
  }

  return aps;
}
