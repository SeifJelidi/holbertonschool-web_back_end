export default function getStudentsByLocation(MyArr, city) {
  let s1 = MyArr.filter((i) => i.location === city);
  return s1;
}
