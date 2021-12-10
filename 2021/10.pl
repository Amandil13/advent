#!//usr/bin/perl
use strict;
use warnings;

#open(my $fh, '<', '10.sample');
open(my $fh, '<', '10.in');
my @input;
foreach my $line (<$fh>){ 
    chomp($line);
    push @input,$line;
} 
my $score = 0;
my @incomplete;
foreach my $line (@input){ 
    while ($line =~ m/(\(\)|\<\>|\[\]|\{\})/){ 
        $line =~ s/(\(\)|\<\>|\[\]|\{\})//;
    } 
    my $copy = $line;
    $copy =~ s/[\(\[\{\<]*//g;
    if ($copy =~ m/^(.)/){
        my $char = $1;
        if ($char eq ')'){ 
            $score += 3;
        } elsif ($char eq ']'){ 
            $score += 57;
        } elsif ($char eq '}'){ 
            $score += 1197;
        } elsif ($char eq '>'){ 
            $score += 25137;
        } 
    } else { 
        push @incomplete,$line 
    }
} 

my @scores;
foreach my $line (@incomplete){ 
    my $linescore = 0;
    foreach my $char (split //, reverse($line)) {
         $linescore *= 5;
        if ($char eq '('){ 
            $linescore += 1;
        } elsif ($char eq '['){ 
            $linescore += 2;
        } elsif ($char eq '{'){ 
            $linescore += 3;
        } elsif ($char eq '<'){ 
            $linescore += 4;
        } 
    }
    push @scores,$linescore;
} 

my $l = (scalar @scores - 1) /2;
my @sorted = sort { $a <=> $b } @scores;
print "part 1: $score\n";
print "part 2: $sorted[$l]\n";
