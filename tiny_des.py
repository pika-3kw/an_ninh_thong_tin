def expand(bit):
  return "{0}{1}{2}{3}{4}{5}".format(bit[2],bit[3],bit[1],bit[2],bit[1],bit[0])


def compress(bit):
  return "{0}{1}{2}{3}{4}{5}".format(bit[5],bit[1],bit[3],bit[2],bit[7],bit[0])


def p_box(bit):
  return '{0}{1}{2}{3}'.format(bit[2],bit[0],bit[3],bit[1])


def s_box(bit):
  table = [
    ["1110", '0100', '1101', '0001', '0010', '1111', '1011', '1000', '0011', '1010', '0110', '1100', '0101', '1001', '0000', '0111'],
    ['0000', '1111', '0111', '0100', '1110', '0010', '1101', '0001', '1010', '0110', '1100', '1011', '1001', '0101', '0011', '1000'],
    ['0100', '0001', '1110', '1000', '1101', '0110', '0010', '1011', '1111', '1100', '1001', '0111', '0011', '1010', '0101', '0000'],
    ['1111', '1100', '1000', '0010', '0100', '1001', '0001', '0111', '0101', '1011', '0011', '1110', '1010', '0000', '0110', '1101']
  ]

  row = int(bit[0]+bit[5],2)
  col = int(bit[1]+bit[2]+bit[3]+bit[4],2)

  return table[row][col]

def dich_trai_1(bit):
  return '{0}{1}{2}{3}'.format(bit[1],bit[2],bit[3],bit[0])

def dich_trai_2(bit):
  return '{0}{1}{2}{3}'.format(bit[2],bit[3],bit[0],bit[1])

def cong(bit1, bit2):
  result = []
  for i in range (len(bit1)):
    if(bit1[i] == bit2[i]):
      result.append('0')
    else: 
      result.append('1')
  return "".join(result) 

# p = "01011100"
# k = "10011010"

p = input("Nhập bản rõ p: ")
k = input("Nhập khoá k: ")

l = ["","","",""]
r = ["","","",""]
kl = ["","","",""]
kr = ["","","", ""]

l[0] = p[0:4]
r[0] = p[4:8]
kl[0] = k[0:4]
kr[0] = k[4:8]


print("L0 = {0}, R0 = {1}".format(l[0], r[0]))

print("KL0 = {0}, KR0 = {1}".format(kl[0], kr[0]))

print('-----')

for i in range(3):
  lap = i+1
  print("Vòng",lap)

  l[lap] = r[i]
  print("L{0} = R{1} = {2}".format(lap,i, l[lap]))
  print("Expand(R{0}) = Expand({1}) = {2}".format(i,r[i],expand(r[i])))
  print()


  if(lap == 2):
    kl[lap] = dich_trai_2(kl[i])
    kr[lap] = dich_trai_2(kr[i])
    print('KL{0} = KL{1} << 1 = {2} << 2 = {3}'.format( lap, i, kl[i], kl[lap]))
    print('KR{0} = KR{1} << 1 = {2} << 2 = {3}'.format(lap, i, kr[i], kr[lap]))
  else:
    kl[lap] = dich_trai_1(kl[i])
    kr[lap] = dich_trai_1(kr[i])
    print('KL{0} = KL{1} << 1 = {2} << 1 = {3}'.format( lap, i, kl[i], kl[lap]))
    print('KR{0} = KR{1} << 1 = {2} << 1 = {3}'.format(lap, i, kr[i], kr[lap]))

  print()
  
  k_lap = compress(kl[lap] + kr[lap])
  print('K{0} = Compress(KL{1}KR{2}) = Compress({3}) = {4}'.format(lap, lap, lap, kl[lap] + kr[lap], k_lap))
  print()

  ek = cong(expand(r[i]), k_lap)
  print(ek)
  print("Expand(R{0}) cong K{1} = {2} cong {3} = {4}".format(i, lap, expand(r[i]), k_lap, ek))
  print()

  print('Tra bảng S-box hàng {0} cột {1}'.format(ek[0]+ek[5], ek[1]+ek[2]+ek[3]+ek[4]))
  
  # sbox = input("S-box({0}) = ".format(ek))
  sbox = s_box(ek)
  print("S-box({0}) = {1}".format(ek, sbox))
  print("Chú ý: đối chiếu lại bảng S-box tránh sai sót")

  f = p_box(sbox)
  print('F{0} = P-box({1}) = {2}'.format(lap, sbox, f))
  print()

  r[lap] = cong(l[i],f)
  print('R{0} = L{1} cong F{2} = {3}'.format(lap, i, lap, r[lap]))
  print('-----')


c = l[3] + r[3]

print("C = L3R3 = {0}".format(c))