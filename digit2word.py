def digittoword(n):
  Words_upto_19=['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
  Words_upto_99=['','','Twenty','Thirty','Fourty','Fifty','Sixty','Seventy','Eighty','Ninety']
  Words_upto_999=['','Hundred','Two Hundred','Three Hundred','Four Hundred','Five Hundred','Six Hundred','Seven Hundred','Eight Hundred','Nine Hundred']
  
  output=''
  if n==0:
    output='Zero'
  elif n<=19:
    output= Words_upto_19[n]
  elif n<=99:
    output= Words_upto_99[n//10]+ " " + Words_upto_19[n%10]
  elif n<=999:
    output= Words_upto_999[n//100]+ " " + Words_upto_99[n%100//10]+ " " + Words_upto_19[n%10]
  else:
    output = "Please enter numbers between 0 to 999"
  return output
  
print(digittoword(n))