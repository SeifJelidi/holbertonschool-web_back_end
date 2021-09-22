export default function getStudentsByLocation(MyArr, city) {
  const s1 = MyArr.filter((i) => i.location === city);
  return s1;
}
