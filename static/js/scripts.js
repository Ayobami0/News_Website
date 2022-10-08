prevBtn = document.getElementById('prev-btn')
nextBtn = document.getElementById('next-btn')
pageNo = document.getElementById('page-no').innerHTMl
maxPage = document.getElementById('max-no').textContent

if (pageNo == 1){
  prevBtn.setAttribute('href', 'javascript:void(0)')
}
if (pageNo == maxPage){
  nextBtn.href = ''
}
