function binary_sum(s,start,stop){
	if (start>=stop){
		return 0 ;
	}
	else if(start == stop){
		return s[start] ;
	}
	else {
		mid = (start+stop)/2 ;

		return binary_sum(s,start,mid)+ binary_sum(s,mid,stop) ;
	}
}

function range(start, end) {
    var number = [];
    for (var i = start; i <= end; i++) {
        number.push(i);
    }
    return number;
}

s = range(1,10);
result = binary_sum(s,1,s.length);

print(result);