export default function getListStudentIds(MyArr) {
  if (!Array.isArray(MyArr)) return [];

  return MyArr.map((item) => item.id);
}
