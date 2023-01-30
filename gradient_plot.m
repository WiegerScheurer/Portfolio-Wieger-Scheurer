function[output] = gradient_plot(input)
sqinput = (input*input);
sqinputcolor = (sqinput-1);

for ii = 1:sqinput;
    color = [(1-(1/sqinputcolor)*(ii-1)),(1-(1/sqinputcolor)*(ii-1)),(1-(1/sqinputcolor)*(ii-1))];
    if sqinputcolor == 0;
    color = [1 1 1];
end
    b = num2str(color,100000);
subplot(input,input,ii)
set(gca,'Color', b );
end