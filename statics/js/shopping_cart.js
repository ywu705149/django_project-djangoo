p1 = document.getElementById('p1');
p2 = document.getElementById('p2');
m1 = document.getElementById('m1');
m2 = document.getElementById('m2');
test1 = document.getElementById('test1').value;
test2 = document.getElementById('test2').value;

p1.addEventListener('click', function(){
    test1.value += 1;
});

p2.addEventListener('click', function(){
    test2.value += 1;
});

m1.addEventListener('click', function(){
    test1.value -= 1;
});

m2.addEventListener('click', function(){
    test2.value -= 1;
});