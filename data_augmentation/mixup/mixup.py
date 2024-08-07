criterion = nn.CrossEntropyLoss()
for x, y in train_loader:
    x, y = x.cuda(), y.cuda()
    # Mixup inputs.
    lam = np.random.beta(alpha, alpha)
    index = torch.randperm(x.size(0)).cuda()
    mixed_x = lam * x + (1 - lam) * x[index, :]
    # Mixup loss.
    pred = model(mixed_x)
    loss = lam * criterion(pred, y) + (1 - lam) * criterion(pred, y[index])
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()